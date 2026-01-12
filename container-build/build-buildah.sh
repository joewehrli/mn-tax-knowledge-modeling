source ./build-buildah.conf

##export BUILDAH_RUNTIME="/usr/bin/runc"
export BUILDAH_RUNTIME="/usr/bin/crun"

make_instance(){
buildah --name $cname from public.ecr.aws/lts/ubuntu:24.04
buildah run $cname -- bash -i -c "DEBIAN_FRONTEND=noninteractive apt-get -y update"
}

make_runtime() {
local REQUIREMENTS="$(tr '\n' ' ' < ./requirements.txt)"
local TODAY=$(date +%Y-%m-%d)
local OUTFILE="requirements-${TODAY}.txt"
buildah run $cname -- bash -i -c "apt-get install -y pip --update"
buildah run $cname -- bash -i -c "apt-get install -y  python3.12-venv"
buildah run $cname -- bash -i -c "python3 -m venv /root/ocipy"
buildah run $cname -- bash -i -c "source /root/ocipy/bin/activate; which python"
buildah run $cname -- bash -i -c "source /root/ocipy/bin/activate; which pip"
buildah run $cname -- bash -i -c "source /root/ocipy/bin/activate; pip install $REQUIREMENTS"
buildah run $cname -- bash -i -c "source /root/ocipy/bin/activate; pip freeze" > $OUTFILE
buildah run $cname -- bash -i -c "apt-get install -y  swi-prolog"
}

: <<'COMMENT'
(type -p wget >/dev/null || (apt update && apt install wget -y)) \
	&& mkdir -p -m 755 /etc/apt/keyrings \
	&& out=$(mktemp) && wget -nv -O$out https://cli.github.com/packages/githubcli-archive-keyring.gpg \
	&& cat $out | tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
	&& chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
	&& mkdir -p -m 755 /etc/apt/sources.list.d \
	&& echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
	&& apt update \
	&& apt install gh -y
COMMENT

: <<'COMMENT'
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
or ARM
curl "https://awscli.amazonaws.com/awscli-exe-linux-aarch64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
COMMENT

: <<'COMMENT'
curl -fsSL https://claude.ai/install.sh | bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc && source ~/.bashrc
COMMENT

: <<'COMMENT'
curl -fsSL https://claude.ai/install.sh | bash
Setting up Claude Code...

✔ Claude Code successfully installed!

  Version: 2.0.42

  Location: ~/.local/bin/claude

  Next: Run claude --help to get started

⚠ Setup notes:
  • Native installation exists but ~/.local/bin is not in your PATH. Run:

  echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc && source ~/.bashrc

Installation complete!
COMMENT

: <<'COMMENT'
# get tyl claude release
# see https://github.com/tyler-technologies/claude-code-with-amazon-bedrock-distribution
./install.sh
COMMENT

: <<'COMMENT'
root@3188c866d331:/workspaces/mn-tax-knowledge-modeling/claude-code-bedrock-20251030_1# ./install.sh 
======================================
Claude Code Authentication Installer
======================================

Organization: sso.tylertech.com

Checking prerequisites...
✓ Prerequisites found (AWS CLI and Claude Code)

Detecting platform and architecture...
✓ Detected Linux x64

Installing authentication tools...

Installing Claude Code settings...
✓ Claude Code telemetry configured with profile ClaudeCodeUnix

Installing OTEL helper...
✓ OTEL helper installed
The OTEL helper will extract user attributes from authentication tokens
and include them in metrics. To test the helper, run:
  /root/claude-code-with-bedrock/otel-helper --test
✓ Using Unix profile: ClaudeCodeUnix

Configuring AWS profile...
✓ AWS profile ClaudeCodeUnix configured

======================================
✓ Installation complete!
======================================
Note: Authentication will automatically open your browser when you run Claude Code.
COMMENT

