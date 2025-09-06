# DogPy

1. create venv: `python3 -m venv .venv`
2. activate `source .venv/bin/activate`
3. install deps: `python3 -m pip install -r requirements.txt`
4. run `python3 __main__.py` or `./__main__.py`

# What is it?

Python documentation helper (e.g. "how do I split a string by spaces?")

## How it works?

1. [smolagents](https://huggingface.co/docs/smolagents/en/index) for Agentic RAG + light formatting of answer
2. Real python docs (retrieved based on your `python3 --version`)
3. Embed each .txt file in docs with some embedding method, store it somehow (maybe add cache)
4. Query documentation through agent -> find relevant doc -> repeat -> output concise answer

## Goals

0. ease of use. Interactive chat mode with highlighting and non-interactive cli raw text output.
1. speed. It has to be faster than googling and waiting for gemini to generate explanation
2. quality. It has to have knowledge required to assist with Leetcode/Advent of Code type programs, no 100% compatibility, indigenious knowledge.
3. local first / offline mode. Fallback to ollama (maybe solely focus on it if this does not sacrifice quality and speed too much)


# Research goals

0. actually read references 3-6
1. Compare complexity of task to LIMIT [^1] dataset 
2. Explore how HyDE [^2] increase quality 
3. Explore how Instruction-Trained Retrievers [^3] increase quality 
4. Compare with multi-vector [^5][^6] and lexical search [^4]
5. Formalize task, find cherry picks and assemble dataset




[^1] On the Theoretical Limitations of Embedding-Based Retrieval
```bibtex
@misc{weller2025theoreticallimitationsembeddingbasedretrieval,
      title={On the Theoretical Limitations of Embedding-Based Retrieval}, 
      author={Orion Weller and Michael Boratko and Iftekhar Naim and Jinhyuk Lee},
      year={2025},
      eprint={2508.21038},
      archivePrefix={arXiv},
      primaryClass={cs.IR},
      url={https://arxiv.org/abs/2508.21038}, 
}
```

[^2] Precise Zero-Shot Dense Retrieval without Relevance Labels
```bibtex
@misc{gao2022precisezeroshotdenseretrieval,
      title={Precise Zero-Shot Dense Retrieval without Relevance Labels}, 
      author={Luyu Gao and Xueguang Ma and Jimmy Lin and Jamie Callan},
      year={2022},
      eprint={2212.10496},
      archivePrefix={arXiv},
      primaryClass={cs.IR},
      url={https://arxiv.org/abs/2212.10496}, 
}
```

[^3] Promptriever: Instruction-Trained Retrievers Can Be Prompted Like Language Models
```bibtex
@misc{weller2024promptrieverinstructiontrainedretrieversprompted,
      title={Promptriever: Instruction-Trained Retrievers Can Be Prompted Like Language Models}, 
      author={Orion Weller and Benjamin Van Durme and Dawn Lawrie and Ashwin Paranjape and Yuhao Zhang and Jack Hessel},
      year={2024},
      eprint={2409.11136},
      archivePrefix={arXiv},
      primaryClass={cs.IR},
      url={https://arxiv.org/abs/2409.11136}, 
}
```

[^4] Okapi at TREC-3
```bibtex
@article{robertson1995okapi,
  title={{Okapi at TREC-3}},
  author={Robertson, Stephen E and Walker, Stephen and Hancock-Beaulieu, Micheline M and Gatford, Mark},
  journal={Proceedings of the Third Text REtrieval Conference (TREC-3)},
  year={1995},
  pages={109--122}
}
```

[^5] Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference
```bibtex
@misc{modernbert,
      title={Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference}, 
      author={Benjamin Warner and Antoine Chaffin and Benjamin Clavié and Orion Weller and Oskar Hallström and Said Taghadouini and Alexis Gallagher and Raja Biswas and Faisal Ladhak and Tom Aarsen and Nathan Cooper and Griffin Adams and Jeremy Howard and Iacopo Poli},
      year={2024},
      eprint={2412.13663},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2412.13663}, 
}

```

[^6] Nomic Embed: Training a Reproducible Long Context Text Embedder
```bibtex
@misc{nussbaum2024nomic,
      title={Nomic Embed: Training a Reproducible Long Context Text Embedder}, 
      author={Zach Nussbaum and John X. Morris and Brandon Duderstadt and Andriy Mulyar},
      year={2024},
      eprint={2402.01613},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
