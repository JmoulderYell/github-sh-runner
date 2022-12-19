FROM ubuntu:latest
RUN apt update && apt upgrade -y && apt install -y systemctl curl wget sudo python3 python3-pip
RUN pip3 install requests
RUN mkdir /gh-actions-runner && cd /gh-actions-runner
RUN curl -o /tmp/actions-runner-linux-x64-2.tar.gz -L https://github.com/actions/runner/releases/download/v2.300.0/actions-runner-linux-x64-2.300.0-noexternals.tar.gz
RUN tar vxzf /tmp/actions-runner-linux-x64-2.tar.gz -C /gh-actions-runner && rm /tmp/actions-runner-linux-x64-2.tar.gz
COPY / /gh-actions-runner/
WORKDIR /gh-actions-runner
RUN chmod 777 -R /gh-actions-runner
RUN cp /gh-actions-runner/runner.service /etc/systemd/system/runner.service
RUN useradd -s /bin/bash -d /home/github/ -m -G sudo github
RUN echo "a\na" | passwd -q github
USER github
RUN echo "a" | sudo -S /gh-actions-runner/bin/installdependencies.sh

CMD [ "/gh-actions-runner/runner.sh" ]
