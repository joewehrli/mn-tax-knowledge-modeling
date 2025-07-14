## make the dev container

From a shell
avm@joe8:~/extdata/repos-ai/mn-tax-knowledge-modeling$
```
cd container-build
source build-buildah.conf
source build-buildah.sh
make_instance
make_runtime
# commit
buildah commit $cname $cname-devcon:0001
```
