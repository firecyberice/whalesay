```
______________
< Hello Docker >
--------------
   \
    \
     \
                   ##         .
             ## ## ##        ==
          ## ## ## ## ##    ===
      /"""""""""""""""""\___/ ===
 ~~~ {~~ ~~~~ ~~~ ~~~~ ~~~ ~ /  ===- ~~~
      \______ o           __/
        \    \         __/
         \____\_______/

```
### Usage:

#### Whalesay only

`docker run --rm firecyberice/whalesay Hello Docker`

#### Whalesay with web API

`docker run -d --rm --name whaleweb -v /var/run/docker.sock:/var/run/docker.sock -P firecyberice/whalesay:web`

`docker run --rm --link whaleweb alpine:3.2 bin/sh -c "apk add --update curl && curl -sL 'http://whaleweb:5000/message/Hello%20Hypriot'"`

### Links:

[Dockerfile](https://github.com/firecyberice/whalesay/blob/master/Dockerfile)

[Build Repo](https://github.com/firecyberice/whalesay)


[Whale Source](https://github.com/moxiegirl/whalesay)

[Cowsay source](https://github.com/jasonm23/cowsay)
