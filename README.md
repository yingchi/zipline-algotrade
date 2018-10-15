# Zipline-algotrade
### Environment Setup Memo
1. Create a specific Python virtual envirnoment for it `conda create -n zipline python=3.5 jupyter`
> Note: ensure python is < 3.5.0, and remember to install jupyter together
2. Activate the environment `source activate zipline`
3. Install zipline `conda install -c Quantopian zipline`
4. Install matplotlib `conda install matplotlib`

### Ingest Data Bundles
To run any zipline strategies, we need to ingest a data bundle first.
To use Quandl data bundle, you need to apply an account to acquire an API.
Then,
```shell
QUANDL_API_KEY=<yourkey> 
zipline ingest -b quantopian-quandl
```