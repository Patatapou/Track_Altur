---
license: mit
tags:
  - audio
  - anti-spoofing
  - audio-deepfake-detection
  - speech
  - asvspoof
  - wav2vec2
---

# W2V2-AASIST

[![EER% 0.22 on ASVspoof2019_LA](https://img.shields.io/badge/EER%25%20on%20ASVspoof2019__LA-0.22%25-brightgreen)](https://huggingface.co/spaces/SpeechAntiSpoofingBenchmarks/SpeechAntiSpoofingArena?system=w2v2-aasist)
[![EER% 8.11 on ASVspoof2021_LA](https://img.shields.io/badge/EER%25%20on%20ASVspoof2021__LA-8.11%25-green)](https://huggingface.co/spaces/SpeechAntiSpoofingBenchmarks/SpeechAntiSpoofingArena?system=w2v2-aasist)
[![EER% 8.32 on ASVspoof2021_DF](https://img.shields.io/badge/EER%25%20on%20ASVspoof2021__DF-8.32%25-green)](https://huggingface.co/spaces/SpeechAntiSpoofingBenchmarks/SpeechAntiSpoofingArena?system=w2v2-aasist)
[![EER% 11.22 on InTheWild](https://img.shields.io/badge/EER%25%20on%20InTheWild-11.22%25-green)](https://huggingface.co/spaces/SpeechAntiSpoofingBenchmarks/SpeechAntiSpoofingArena?system=w2v2-aasist)
[![EER% 38.57 on CD-ADD](https://img.shields.io/badge/EER%25%20on%20CD--ADD-38.57%25-orange)](https://huggingface.co/spaces/SpeechAntiSpoofingBenchmarks/SpeechAntiSpoofingArena?system=w2v2-aasist)
[![EER% 46.12 on SONAR](https://img.shields.io/badge/EER%25%20on%20SONAR-46.12%25-lightgrey)](https://huggingface.co/spaces/SpeechAntiSpoofingBenchmarks/SpeechAntiSpoofingArena?system=w2v2-aasist)
[![EER% 11.21 on LibriSeVoc](https://img.shields.io/badge/EER%25%20on%20LibriSeVoc-11.21%25-lightgrey)](https://huggingface.co/spaces/SpeechAntiSpoofingBenchmarks/SpeechAntiSpoofingArena?system=w2v2-aasist)
[![EER% 17.28 on CFAD](https://img.shields.io/badge/EER%25%20on%20CFAD-17.28%25-lightgrey)](https://huggingface.co/spaces/SpeechAntiSpoofingBenchmarks/SpeechAntiSpoofingArena?system=w2v2-aasist)
[![EER% 21.79 on CVoiceFake_small](https://img.shields.io/badge/EER%25%20on%20CVoiceFake__small-21.79%25-lightgrey)](https://huggingface.co/spaces/SpeechAntiSpoofingBenchmarks/SpeechAntiSpoofingArena?system=w2v2-aasist)
[![EER% 16.25 on ASVspoof5](https://img.shields.io/badge/EER%25%20on%20ASVspoof5-16.25%25-lightgrey)](https://huggingface.co/spaces/SpeechAntiSpoofingBenchmarks/SpeechAntiSpoofingArena?system=w2v2-aasist)
[![EER% 45.06 on DeepVoice](https://img.shields.io/badge/EER%25%20on%20DeepVoice-45.06%25-lightgrey)](https://huggingface.co/spaces/SpeechAntiSpoofingBenchmarks/SpeechAntiSpoofingArena?system=w2v2-aasist)
[![EER% 30.98 on ArAD](https://img.shields.io/badge/EER%25%20on%20ArAD-30.98%25-lightgrey)](https://huggingface.co/spaces/SpeechAntiSpoofingBenchmarks/SpeechAntiSpoofingArena?system=w2v2-aasist)
[![EER% 9.57 on DECRO](https://img.shields.io/badge/EER%25%20on%20DECRO-9.57%25-yellow)](https://huggingface.co/spaces/SpeechAntiSpoofingBenchmarks/SpeechAntiSpoofingArena?system=w2v2-aasist)
[![EER% 26.17 on J-SPAW_LA](https://img.shields.io/badge/EER%25%20on%20J--SPAW__LA-26.17%25-lightgrey)](https://huggingface.co/spaces/SpeechAntiSpoofingBenchmarks/SpeechAntiSpoofingArena?system=w2v2-aasist)
[![EER% 39.22 on ODSS](https://img.shields.io/badge/EER%25%20on%20ODSS-39.22%25-lightgrey)](https://huggingface.co/spaces/SpeechAntiSpoofingBenchmarks/SpeechAntiSpoofingArena?system=w2v2-aasist)
[![EER% 7.11 on HABLA](https://img.shields.io/badge/EER%25%20on%20HABLA-7.11%25-yellow)](https://huggingface.co/spaces/SpeechAntiSpoofingBenchmarks/SpeechAntiSpoofingArena?system=w2v2-aasist)
[![EER% 11.92 on DFADD](https://img.shields.io/badge/EER%25%20on%20DFADD-11.92%25-lightgrey)](https://huggingface.co/spaces/SpeechAntiSpoofingBenchmarks/SpeechAntiSpoofingArena?system=w2v2-aasist)
[![EER% 3.01 on PyAra](https://img.shields.io/badge/EER%25%20on%20PyAra-3.01%25-green)](https://huggingface.co/spaces/SpeechAntiSpoofingBenchmarks/SpeechAntiSpoofingArena?system=w2v2-aasist)
[![EER% 24.14 on XMAD](https://img.shields.io/badge/EER%25%20on%20XMAD-24.14%25-lightgrey)](https://huggingface.co/spaces/SpeechAntiSpoofingBenchmarks/SpeechAntiSpoofingArena?system=w2v2-aasist)
[![1-SRR% 28.06 on LRLspoof](https://img.shields.io/badge/1--SRR%25%20on%20LRLspoof-28.06%25-lightgrey)](https://huggingface.co/spaces/SpeechAntiSpoofingBenchmarks/SpeechAntiSpoofingArena?system=w2v2-aasist)
[![EER% 14.8 on ADD22_eval_31](https://img.shields.io/badge/EER%25%20on%20ADD22__eval__31-14.8%25-lightgrey)](https://huggingface.co/spaces/SpeechAntiSpoofingBenchmarks/SpeechAntiSpoofingArena?system=w2v2-aasist)
[![EER% 27.75 on ADD2023_track12_test_r1](https://img.shields.io/badge/EER%25%20on%20ADD2023__track12__test__r1-27.75%25-lightgrey)](https://huggingface.co/spaces/SpeechAntiSpoofingBenchmarks/SpeechAntiSpoofingArena?system=w2v2-aasist)
[![EER% 1.34 on EmoFake_test](https://img.shields.io/badge/EER%25%20on%20EmoFake__test-1.34%25-brightgreen)](https://huggingface.co/spaces/SpeechAntiSpoofingBenchmarks/SpeechAntiSpoofingArena?system=w2v2-aasist)
[![1-SRR% 70.98 on EmoSpoofTTS](https://img.shields.io/badge/1--SRR%25%20on%20EmoSpoofTTS-70.98%25-lightgrey)](https://huggingface.co/spaces/SpeechAntiSpoofingBenchmarks/SpeechAntiSpoofingArena?system=w2v2-aasist)
[![arena tier](https://img.shields.io/endpoint?url=https://speechantispoofingbenchmarks-speechantispoofingarena.hf.space/badge/w2v2-aasist/tier.json)](https://huggingface.co/spaces/SpeechAntiSpoofingBenchmarks/SpeechAntiSpoofingArena?system=w2v2-aasist)
[![arena rank](https://img.shields.io/endpoint?url=https://speechantispoofingbenchmarks-speechantispoofingarena.hf.space/badge/w2v2-aasist/rank.json)](https://huggingface.co/spaces/SpeechAntiSpoofingBenchmarks/SpeechAntiSpoofingArena?system=w2v2-aasist)

A **wav2vec 2.0 (XLS-R 300M) + AASIST** anti-spoofing model, from
*"Automatic speaker verification spoofing and deepfake detection using wav2vec 2.0
and data augmentation"* (Tak, Todisco, Wang, Jung, Yamagishi & Evans, Odyssey 2022).
A self-supervised XLS-R front-end is fine-tuned end-to-end with an AASIST
spectro-temporal graph-attention back-end. The model takes a raw speech waveform
and returns a score where **higher = more bona fide**.

- **Code:** https://github.com/TakHemlata/SSL_Anti-spoofing
- **Paper:** https://arxiv.org/abs/2202.12233
- **Parameters:** 317,837,800 (317.84 M)
- **Checkpoint:** [`LA_model.pth`](./LA_model.pth) (the LA variant)

The exact wrapper used to produce the Arena scores is in
[`w2v2_aasist.py`](./w2v2_aasist.py); the network definition is in
[`_net.py`](./_net.py).

## Architecture

1. **wav2vec 2.0 XLS-R (300M) front-end** — a self-supervised transformer
   (`fairseq` `Wav2Vec2Model`) producing 1024-d frame features, fine-tuned
   end-to-end with the rest of the network.
2. **AASIST back-end** — the XLS-R features are projected to 128-d, max-pooled,
   passed through a RawNet2-style residual encoder, then heterogeneous stacking
   graph-attention layers (HS-GAL) over spectral and temporal sub-graphs with a
   learnable master node and graph pooling.
3. The 2-logit output is read at **index 1 = bona fide**.

## How it was trained

- **Data:** ASVspoof 2019 **Logical Access (LA)**, with RawBoost data augmentation.
- **Input length:** raw audio at 16 kHz cropped/padded to 64,600 samples (~4.04 s).
- **Output:** 2-class logits; the bona-fide logit (index 1) is the score.

See the [source repository](https://github.com/TakHemlata/SSL_Anti-spoofing) for the
full training and evaluation code.

## Benchmark result (Speech Anti-Spoofing Arena)

Evaluated through the reproducible [Speech Anti-Spoofing Arena](https://huggingface.co/spaces/SpeechAntiSpoofingBenchmarks/SpeechAntiSpoofingArena?system=w2v2-aasist).
Scores were computed with a **deterministic first-64,600-sample window** (no random
crop), so the numbers are exactly reproducible from the pinned score file.

| Dataset | Split | EER % | Trials | Skipped | Notes |
|---|---|---|---|---|---|
| ASVspoof2019_LA | test | **0.22** | 71,237 | 0 | in-domain (training data) |
| ASVspoof2021_LA | test | **8.11** | 181,566 | 0 | cross-dataset generalization |
| ASVspoof2021_DF | test | **8.32** | 611,829 | 0 | cross-dataset generalization |
| InTheWild | test | **11.22** | 31,779 | 0 | out-of-domain (real-world deepfakes) |
| CD-ADD | test | **38.57** | 20,786 | 0 | out-of-domain (modern neural-TTS) |
| SONAR | test | **46.12** | 3,948 | 0 | out-of-domain (diverse deepfake sources) |
| LibriSeVoc | test | **11.21** | 18,487 | 0 | out-of-domain (LibriTTS neural vocoders) |
| CFAD | test | **17.28** | 62,999 | 0 | out-of-domain (Chinese fake-audio detection) |
| CVoiceFake_small | test | **21.79** | 138,136 | 0 | out-of-domain (multilingual vocoded TTS) |
| ASVspoof5 | test | **16.25** | 680,774 | 0 | out-of-domain (crowdsourced TTS/VC + adversarial) |

The self-supervised XLS-R front-end generalizes markedly better to unseen attacks
than raw-waveform baselines — most strikingly on **InTheWild (11.22 %)** and
**CD-ADD (38.57 %)**, where lightweight CNN models degrade much further.

## Usage

The checkpoint is a `state_dict` for the `Model` network defined in
[`_net.py`](./_net.py). Constructing the network requires the base XLS-R 300M
checkpoint **`xlsr2_300m.pt`** next to the wrapper (only used to build the
wav2vec 2.0 architecture; every weight is then overwritten by `LA_model.pth`):

```bash
wget https://dl.fbaipublicfiles.com/fairseq/wav2vec/xlsr2_300m.pt
```

The input **must** be exactly 64,600 samples at 16 kHz mono — window the waveform
with `pad_fixed` (first 64,600 samples, tile-repeat if shorter).

```python
import numpy as np
from w2v2_aasist import W2V2AASIST   # _net.py + w2v2_aasist.py are in this repo

m = W2V2AASIST()
m.load()                                          # loads LA_model.pth (+ xlsr2_300m.pt)
audio = np.random.randn(48000).astype(np.float32) # float32 mono 16 kHz
print(m.score_batch([audio], [16000])[0])         # higher = more bona fide
m.unload()
```

Internally the wrapper windows the input, runs the network, and returns
`logits[:, 1]` (class 1 = bona fide). [`w2v2_aasist.py`](./w2v2_aasist.py) is the
exact `speech_spoof_bench` model that produced the Arena `scores.txt`.

## Citation

**This model / paper:**

```bibtex
@inproceedings{tak2022automatic,
  title={Automatic speaker verification spoofing and deepfake detection using wav2vec 2.0 and data augmentation},
  author={Tak, Hemlata and Todisco, Massimiliano and Wang, Xin and Jung, Jee-weon and Yamagishi, Junichi and Evans, Nicholas},
  booktitle={The Speaker and Language Recognition Workshop (Odyssey 2022)},
  pages={112--119},
  year={2022}
}
```

**AASIST back-end:**

```bibtex
@inproceedings{jung2022aasist,
  title={{AASIST}: Audio Anti-Spoofing Using Integrated Spectro-Temporal Graph Attention Networks},
  author={Jung, Jee-weon and Heo, Hee-Soo and Tak, Hemlata and Shim, Hye-jin and Chung, Joon Son and Lee, Bong-Jin and Yu, Ha-Jin and Evans, Nicholas},
  booktitle={ICASSP 2022},
  pages={6367--6371},
  year={2022},
  organization={IEEE}
}
```

## License

MIT — see the [source repository](https://github.com/TakHemlata/SSL_Anti-spoofing).

## Maintainer

Maintained by Kirill Borodin (SpeechAntiSpoofingBenchmarks).
- Email: kborodin.research@gmail.com
- Telegram: [@korallll_ai](https://t.me/korallll_ai)
