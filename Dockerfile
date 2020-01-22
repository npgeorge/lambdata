FROM debian

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get upgrade -y && \
apt-get install python3-pip curl nano -y && \
pip3 install pandas numpy && \
pip3 install -i https://test.pypi.org/simple/ lambdata-npg==0.1.1 && \
python3 -c "import lambdata_npgeorge; print('success yewwww!!!!')"
