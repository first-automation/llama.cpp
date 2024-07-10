from huggingface_hub import snapshot_download

if __name__ == '__main__':
    model_id="elyza/ELYZA-japanese-Llama-2-7b-instruct"
    snapshot_download(
        repo_id=model_id,
        local_dir="models/ELYZA-japanese-Llama-2-7b-instruct",
        local_dir_use_symlinks=False,
        revision="main"
    )

