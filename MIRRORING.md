two-way mirroring of the repository
===================================

The canonical repository can be found at https://git.iem.at/pd/pd.iem.sh/

For your convenience, there's a two-way mirror on https://github.com/pd-projects/hugo-puredata.info
(*two-way mirror* means, that any changes to the canonical repository are automatically pushed to the github mirror.
Any commits to the github mirror are automatically pushed to the canonical repository.)


# setting up the mirror

these are just private notes so i remember how to update the mirroring

## git.iem.at -> github

### create a private access token on GitHub
1. go to https://github.com/settings/personal-access-tokens
2. Click on `Generate new token`
3. give a nice name
4. keep yourself as the resource owner
5. add expiration and description as needed
6. `Only select repositories` -> **`pd-projects/hugo-puredata.info`**
7. Repository permissions
   - Read access to `Metadata`
   - Read and Write access to `Content` (commits,...)
8. create the token
9. remember the token value as `${ghtoken}`

### setup the push

1. Go to https://git.iem.at/pd/pd.iem.sh/-/settings/repository#js-push-remote-settings
2. `Add new` for a new PUSH repository
3. configure as follows
   | key | value |
   |-----|-------|
   | Git repository URL    | https://github.com/pd-projects/hugo-puredata.info.git |
   | Mirror direction      | `PUSH` |
   | Authentication method | `Username and Password` |
   | Username              | the user name  (resource owner?) used to generate the private token
   | Password              | `${ghtoken}` |



## github -> git.iem.at

### setup a push token for the repository
1. Go to https://git.iem.at/pd/pd.iem.sh/-/settings/access_tokens
2. create a new token with a meaningful name and description
  | name | value |
  |------|-------|
  | Expiration date | ...                |
  | role            | `Developer`        |
  | Scopes          | `write_repository` |
3. remember the token as `${iemtoken}`

### setup a mirror configuration on git.iem.at
1. On https://git.iem.at/zmoelnig/github-mirror/-/settings/ci_cd#js-cicd-variables-settings add a new variable
   | name | value |
   |------|-------|
   | Type | `File |
   | Key  | `MIRROR_CONFIGURATION` |
2. The content is something like

   ```ini
   [pd.iem.sh]
   src = https://github.com/pd-projects/hugo-puredata.info.git
   dst = https://mirror:${iemtoken}@git.iem.at/pd/pd.iem.sh.git
   ```

   The `${iemtoken}` as generated above


### setup a webhook on git.iem.at

1. On https://git.iem.at/zmoelnig/github-mirror/-/settings/ci_cd to to `Pipeline Trigger tokens`
2. Add a new token (with a nice name and expiration date)
3. remember the token value as `${webhooktoken}` (and the project ID)


### configure github to emit the webhook

1. visit https://github.com/pd-projects/hugo-puredata.info/settings/hooks/
2. `Add webhook`
3. Under payload URL enter `https://git.iem.at/api/v4/projects/${projectid}/ref/main/trigger/pipeline?token=${webhooktoken}&variables[REPO]=pd.iem.sh
   - with `${webhooktoken}` being the token you obtained when creating the webhook on git.iem.at
   - with `${projectid}` being the (numeric) project ID of the https://git.iem.at/zmoelnig/github-mirror/ project
4. more configuration:
   | key | value |
   | Content type | `application/json` |
   | Secret | `` (empty) |
   | Enable SSL verification | `true`
   | events | Just the `push` event |
   | Active | `true`
