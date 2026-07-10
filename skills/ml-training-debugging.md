# Skill: ML Training Debugging — la cascada es narrativa, no lista

*(ES) Patrones de debugging de entrenamiento de modelos destilados de meses de crashes reales en GPUs gratuitas y ajenas: leer cascadas como narrativa, compatibilidad de hardware ANTES de tocar código, checkpoints que sobreviven a la plataforma, y las fallas silenciosas que más cuestan.*

**Use when:** a training run crashes, hangs, produces NaN, silently dies, or must survive free-tier/cloud platforms (Kaggle, Colab, spot instances) that kill jobs without warning.

---

Every rule below was paid for with a real crash. None is theoretical.

## 1. Read the cascade as a narrative, not a list

Consecutive errors are almost never independent. A typical real chain: OOM → checkpoint corrupted mid-write → CheckpointError on resume → CUDA illegal address. The third error is not a new bug — it is the *ghost* of the first. **Method:** when errors accumulate, stop fixing the newest one. Order them chronologically and ask of each: "is this a cause, or a consequence of the previous one?" Fix the root; the ghosts evaporate.

## 2. Hardware compatibility BEFORE code (the 2-minute check that saves days)

The GPU decides what your code may do. Verify compute capability FIRST — then choose dtypes and libraries:

- **bf16 requires Ampere+ (sm_80).** On T4 (sm_75) or P100 (sm_60): fp16 + GradScaler. bf16 configs fail late and cryptically.
- **4-bit quantization (bitsandbytes NF4) does not run on Pascal (P100/sm_60)** — it dies at weight-load with `named symbol not found ... ops.cu` in ~2 minutes. If your platform can assign different GPUs, **pin the machine type explicitly in job metadata** — an omitted field means the platform chooses for you, and it chooses wrong.
- **GradScaler requires fp32 master weights.** "Attempting to unscale FP16 gradients" means your trainable params are fp16 — with a big model on small VRAM, that's the signal to switch to LoRA/QLoRA (frozen quantized base + small fp32 adapters) instead of fighting the scaler.

## 3. Checkpoints: off-box, verified, and honest about units

- **Persist OFF the machine** (a model hub, object storage) every N updates. Free-tier boxes die daily; a checkpoint on the box dies with it.
- **Resume must be self-contained:** weights + optimizer state + scaler state + step counter in ONE artifact, plus a tiny `latest.json` (step, loss) you can poll remotely to monitor without opening the platform.
- **Verify by reading back, not by trusting the upload log.** If a resume looks desynced, download the artifact and read the actual step inside. Calm comes from looking.
- **Count real optimizer updates, not micro-batches.** With gradient accumulation, "20,000 steps" may be 625 updates — every schedule (warmup, cosine, checkpoint cadence) silently wrong by 32×.

## 4. Silent failures — the most expensive class

- **Loading weights… 97% … then a bare prompt** = OOM killed by the OS, no traceback. Check `dmesg`/exit code; don't stare at the script.
- **NaN loss handling:** skip the micro-batch WITHOUT touching accumulated grads; let the scaler's step-skip do its job; if ALL micro-batches in an update are NaN, zero grads and continue. Never `loss.backward()` a NaN "just to keep going".
- **Distribution collapse check:** every ~100 updates, softmax the last logits and look at top-p and entropy. A model can keep lowering loss while collapsing — loss alone lies.
- **Secrets/services fail differently under API-triggered jobs than interactive ones.** Verify auth INSIDE the job at startup (whoami-style assert) with a controlled fallback — not at first use, 3 hours in.

## 5. Data pipeline traps

- **Preprocessing that silently discards:** log the count in vs out. A filter that drops 99.9% of your dataset will happily train on the 0.1% and report healthy loss.
- **Sequence packing:** append EOS per document ONCE (watch double-EOS when combining with FIM or other transforms); never cut documents mid-token-sequence into the next batch without knowing you're doing it.
- **A tiny dataset recycled N times is memorization with a good-looking curve.** Tokens-seen ÷ unique-tokens = your real epoch count. Know it.
- **Encoding at the edges:** JSON metadata written by Windows tooling may carry a BOM that breaks strict parsers downstream (`Expecting value: line 1 column 1`). Write UTF-8 *without* BOM for anything a program will read.

## 6. Platform discipline (free tiers & shared clouds)

- Quotas are per-account and reset on a schedule — design runs to die-and-resume gracefully rather than to finish in one sitting.
- Job metadata is a contract: machine type, internet access, attached data — explicit, versioned next to the code.
- Monitor via API (job status + your `latest.json`), not by keeping a browser tab alive.

## The meta-rule

**Verify the consequence, not the intention.** "It should be saving checkpoints" is an intention. Downloading the checkpoint and reading step 750 inside it is a consequence. Between a plausible explanation and a verified one, the plausible one is worth nothing — every scar in this file came from believing an intention.
