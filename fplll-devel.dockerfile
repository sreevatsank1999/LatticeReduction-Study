FROM docker.io/fplll/fpylll:0.6.1

ARG DOCKER_LANG=en_US
ARG DOCKER_TIMEZONE=America/Los_Angeles

ENV LANG=${DOCKER_LANG}.UTF-8 \
    LANGUAGE=${DOCKER_LANG}:UTF-8 \
    LC_ALL=${DOCKER_LANG}.UTF-8

# Creating a user
ARG USERNAME=lll
ARG UID=1000

RUN adduser --no-create-home --gecos "" -u ${UID} ${USERNAME}
RUN adduser ${USERNAME} sudo
RUN passwd -d ${USERNAME}
RUN echo "$DOCKER_TIMEZONE" > /etc/timezone && \
    ln -s -f /usr/share/zoneinfo/$DOCKER_TIMEZONE /etc/localtime

# RUN usermod -l ${USERNAME} $(id -un 1000) && \
#     groupmod -n ${USERNAME} $(id -gn 1000) && \
#     usermod -d /home/${USERNAME} -m ${USERNAME}

# Set user specific environment variables
ENV USER ${USERNAME}
ENV HOME /home/${USERNAME}
WORKDIR /home/${USERNAME}
# Switch to user
USER ${USERNAME}


ENTRYPOINT [  ]
CMD [ "tail", "-f", "/dev/null" ]