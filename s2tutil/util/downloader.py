import sys
import urllib.request as request
from os import path, environ, makedirs

MODELS_URL = {
    model_type: f"https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-{model_type}.bin"
    for model_type in (
        "tiny.en",
        "tiny",
        "base.en",
        "base",
        "small.en",
        "small",
        "medium.en",
        "medium",
        "large-v1",
        "large",
    )
}

_data_home = environ.get(
    "XDG_DATA_HOME",
    path.join(path.expanduser(path.expandvars("$HOME")), ".local", "share"),
)


def download_model(model_name: str, basedir: str = None) -> str:  # pragma: no cover
    """Download a preconverted model from a given model name.

    Currently it doesn't support custom preconverted models yet. PRs are welcome.

    Args:
        model_name (str): Name of the preconverted model.
        basedir (str, optional): Base directory to store the model. Defaults to XDG_DATA_HOME/whispercpp

    Returns:
        The path to the downloaded model.
    """
    if basedir is None:
        basedir = _data_home
    models_dirs = path.join(basedir, "whispercpp")
    if not path.exists(models_dirs):  # pragma: no cover
        makedirs(models_dirs, exist_ok=True)

    model_path = path.join(models_dirs, f"ggml-{model_name}.bin")
    if not path.exists(model_path):
        sys.stderr.write(f"Downloading model {model_name}. It may take a while...")
        request.urlretrieve(MODELS_URL[model_name], model_path)
        sys.stderr.flush()
    return model_path
