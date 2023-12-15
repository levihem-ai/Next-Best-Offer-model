echo "Loading saiga 7b"
mkdir -p data/models/7B/saiga2/
wget https://huggingface.co/IlyaGusev/saiga2_7b_gguf/resolve/main/model-q4_K.gguf -o data/models/7B/saiga2/model-q4_K.gguf

echo "Loading saiga 13b"
mkdir -p data/models/13B/saiga2/
wget https://huggingface.co/IlyaGusev/saiga2_13b_gguf/resolve/main/model-q4_K.gguf -o data/models/13B/saiga2/model-q4_K.gguf

echo "Loading saiga-mistral"
mkdir -p data/models/7B/saiga_mistral/
wget https://huggingface.co/IlyaGusev/saiga_mistral_7b_gguf/resolve/main/model-q4_K.gguf -o data/models/7B/saiga_mistral/model-q4_K.gguf
