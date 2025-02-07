import os
from n41 import load_nekocabocha_chunk
from n43 import chunk_include_pos

OUTPUT_FILE_NAME = "verb_case_patterns.txt"

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def extract_verb_case_patterns():
    with open(OUTPUT_FILE_NAME, mode="w") as f:
        for chunks in load_nekocabocha_chunk():
            for chunk in chunks:
                if chunk.srcs == []:
                    continue
                if not chunk_include_pos(chunk, "動詞"):
                    continue
                if not any([chunk_include_pos(chunks[i], "助詞") for i in chunk.srcs]):
                    continue
                verb = extract_morph_from_chunk_by_pos(chunk, "動詞").base
                particles = " ".join(morph.base for src_i in chunk.srcs for morph in chunks[src_i].morphs if morph.pos == "助詞")
                f.write(f"{verb}\t{particles}\n")

# 1番左を抽出
def extract_morph_from_chunk_by_pos(chank, pos):
    for morph in chank.morphs:
        if morph.pos == pos:
            return morph
    return None

if __name__ == "__main__":
    extract_verb_case_patterns()
