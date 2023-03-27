playground for puredata.info on markdown
========================================

https://pd.iem.sh/

# Workflow

This page uses [`hugo`](https://gohugo.io) to turn a bunch of markdown files (`.md`) into a static webpage.

1. install Hugo: https://gohugo.io/installation/
2. Clone this repository
3. Open a terminal, navigate into the cloned repository
4. Run `hugo server` to startup a live renderer.
   You should see something like this:

   ```
   user@.../pd.iem.sh
   $ hugo server
   Start building sites …
   hugo v0.109.0-7238115e146b21ecbd872ef1c0b08eb7f282fd25 windows/amd64 BuildDate=2022-12-25T17:00:25Z

                      | EN
   -------------------+------
     Pages            | 286
     Paginator pages  |   0
     Non-page files   |   0
     Static files     |  12
     Processed images |   0
     Aliases          |  20
     Sitemaps         |   1
     Cleaned          |   0

   Built in 701 ms
   Watching for changes in ...\pd.iem.sh\{archetypes,content,layouts,static}
   Watching for config changes in ...\pd.iem.sh\config.toml
   Environment: "development"
   Serving pages from memory
   Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
   Web Server is available at //localhost:1313/ (bind address 127.0.0.1)
   Press Ctrl+C to stop
   ```

5. In your browser, open http://localhost:1313/ to get a live preview
   (the actual port number (here `1313` may be different, depending on port availability on your system); it is shown at the end of the output when starting `hugo server`)

6. Edit the `.md` files in the `content/objects/` directory. As soon as you <kbd>save</<kbd> a Markdown file, the live preview will be updated.
7. Once finished, stop the live renderer with <kbd>Ctrl</kbd>-<kbd>C</kbd> (as shown in the startup output)

# GIT repository

## GitHub, git.iem.at, ... WTF?

The canonical repository can be found at https://git.iem.at/pd/pd.iem.sh/

For your convenience, there's a two-way mirror on https://github.com/pd-projects/hugo-puredata.info
(*two-way mirror* means, that any changes to the canonical repository are automatically pushed to the github mirror.
Any commits to the github mirror are automatically pushed to the canonical repository.)

## Issues

Please file any issues,... at the canonical repository at https://git.iem.at/pd/pd.iem.sh/-/issues

## Pull Requests

Feel free to open PRs at the github repository.
Once they are accepted/merged, they will be automatically mirrored to the canonical repository.


# LICENSE
This project is licensed under the BSD-3 license (see [LICENSE.md](./LICENSE.md) for the full text.
