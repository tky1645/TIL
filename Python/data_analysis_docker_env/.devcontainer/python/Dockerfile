# datasience-notebookに対する追加設定
FROM jupyter/datascience-notebook

WORKDIR /tmp/work

COPY requirements.txt ${PWD}

# NOTE: Mac PC で build する場合のみ Rust が必要な模様
# ENV PATH=$PATH:/root/.cargo/bin
# RUN curl https://sh.rustup.rs -sSf > ./rust.sh && bash ./rust.sh -y \
#     && snap install rustup --classic \
#     && rustup install stable

RUN pip install --upgrade pip && pip install -r requirements.txt


