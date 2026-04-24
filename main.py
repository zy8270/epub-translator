from epub_translator import LLM, translate, language, SubmitKind
from tqdm import tqdm

llm = LLM(
    key="喵？", 
    url="https://ark.cn-beijing.volces.com/api/coding/v3",  
    model="doubao-seed-2.0-pro",  
    token_encoding="o200k_base",  
)

with tqdm(total=100, desc="翻译中", unit="%") as pbar:
    last_progress = 0.0

    def on_progress(progress: float):
        global last_progress
        increment = (progress - last_progress) * 100
        pbar.update(increment)
        last_progress = progress

    translate(
        source_path="source.epub",
        target_path="translated.epub",
        target_language="Chinese",
        submit=SubmitKind.REPLACE,
        llm=llm,
        on_progress=on_progress,
        concurrency=1,  
        max_group_tokens=3500,  
        max_retries=5,  
    )