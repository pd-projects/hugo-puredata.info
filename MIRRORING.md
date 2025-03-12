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
9. remember the token value

### setup the push

1. On https://git.iem.at/pd/pd.iem.sh/ go to `Settings` -> `Repository` -> `Mirroring Repository`
2. `Add new` for a new PUSH repository
3. configure as follows
   | key | value |
   |-----|-------|
   | Git repository URL    | https://github.com/pd-projects/hugo-puredata.info.git |
   | Mirror direction      | `PUSH` |
   | Authentication method | `Username and Password` |
   | Username              | the user name  (resource owner?) used to generate the private token
   | Password              | the private token |



## github -> git.iem.at

TODO
