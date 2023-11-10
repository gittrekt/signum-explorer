[![Better Stack Badge](https://uptime.betterstack.com/status-badges/v1/monitor/uiyx.svg)](https://uptime.betterstack.com/?utm_source=status_badge)

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

### Do not use the Cython compiler in master - it's broken
Many functions in Django json core currently have issues causing the compiles to fail
