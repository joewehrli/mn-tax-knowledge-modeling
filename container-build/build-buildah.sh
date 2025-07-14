
source ./build-buildah.conf

export BUILDAH_RUNTIME="/usr/bin/runc"

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
}
