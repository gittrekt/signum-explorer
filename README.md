# Signum Explorer

This documentation is a work in progress. More details to follow.
<br>
<br>
<br>
<br>
<br>
## API Info
```json/SNRinfo/```                   Used to sync multiple explorers to the SNR master so they are all show the same info.<br>
```json/state/123.123.123.123```      Returns node state (ONLINE=1 UNREACHABLE=2 SYNC=3 STUCK=4 FORKED=5). <br>
```json/accounts/```                  Returns top 10 richest accounts. <br>

### Do not use the Cython compiler in master - it's WIP
Many functions from the older explorer code need to  be re-written
