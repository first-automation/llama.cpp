from huggingface_hub import snapshot_download

if __name__ == '__main__':
    #model_id="tokyotech-llm/Llama-3-Swallow-70B-Instruct-v0.1"
    model_id="cyberagent/Llama-3.1-70B-Japanese-Instruct-2407"
    snapshot_download(
        repo_id=model_id,
        local_dir=f"models/{model_id}",
        local_dir_use_symlinks=False,
        revision="main"
    )

