# datasience-notebookに対する追加設定
FROM jupyter/datascience-notebook

WORKDIR /tmp/work
COPY requirements.txt ${PWD}
RUN pip install --upgrade pip && pip install -r requirements.txt
