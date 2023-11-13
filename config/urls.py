from django.conf import settings
from django.urls import include, path

from scan.views.accounts import AccountsListView, AddressDetailView
from scan.views.aliases import AliasListView
from scan.views.assets import (
    AssetDetailView,
    AssetDistributionDetailView,
    AssetHoldersListView,
    AssetListView,
    AssetMintingDetailView,
    AssetTradesListView,
    AssetTransfersListView,
)
from scan.views.ats import AtDetailView, AtListView
from scan.views.blocks import BlockDetailView, BlockListView
from scan.views.cashbacks import CBListView
from scan.views.distribution import DistributionListView
from scan.views.forged_blocks import ForgedBlocksListView
from scan.views.index import index
from scan.views.json import TopAccountsJson, getSNRjson, getStatejson
from scan.views.marketplace import (
    MarketPlaceDetailView,
    MarketPlaceListView,
    MarketPlacePurchasesListView,
)
from scan.views.miners import MinerListView
from scan.views.peers import (
    PeerMonitorDetailView,
    PeerMonitorListView,
    peers_charts_view,
)
from scan.views.pending_transactions import pending_transactions
from scan.views.pools import PoolDetailView, PoolListView
from scan.views.search import search_view
from scan.views.subscriptions import SubscriptionListView
from scan.views.transactions import TxDetailView, TxListView, tx_export_csv

urlpatterns = [
    path("", index, name="index"),
    path("distribution/", DistributionListView.as_view(), name="distribution"),
    path("cbs/", CBListView.as_view(), name="cbs"),
    path("blocks/", BlockListView.as_view(), name="blocks"),
    path("block/<str:height>", BlockDetailView.as_view(), name="block-detail"),
    path("txsPending/", pending_transactions, name="txs-pending"),
    path("txs/", TxListView.as_view(), name="txs"),
    path("tx/<str:id>", TxDetailView.as_view(), name="tx-detail"),
    path("accounts/", AccountsListView.as_view(), name="accounts"),
    path("address/<str:id>", AddressDetailView.as_view(), name="address-detail"),
    path("csv/<str:id>", tx_export_csv, name="account-csv"),
    path("asset/trades", AssetTradesListView.as_view(), name="asset-trades"),
    path("asset/transfers", AssetTransfersListView.as_view(), name="asset-transfers"),
    path("asset/holders", AssetHoldersListView.as_view(), name="asset-holders"),
    path("asset/mintings", AssetMintingDetailView.as_view(), name="asset-mintings"),
    path("asset/distributions", AssetDistributionDetailView.as_view(), name="asset-distributions"),
    path("assets/", AssetListView.as_view(), name="assets"),
    path("asset/<str:id>", AssetDetailView.as_view(), name="asset-detail"),
    path("mps/purchases", MarketPlacePurchasesListView.as_view(), name="mps-purchases"),
    path("mps/", MarketPlaceListView.as_view(), name="mps"),
    path("mp/<str:id>", MarketPlaceDetailView.as_view(), name="mp-detail"),
    path("ats/", AtListView.as_view(), name="ats"),
    path("at/<str:id>", AtDetailView.as_view(), name="at-detail"),
    path("search/", search_view, name="search"),
    path("peers/", PeerMonitorListView.as_view(), name="peers"),
    path("peers-charts/", peers_charts_view, name="peers-charts"),
    path("peer/<str:address>", PeerMonitorDetailView.as_view(), name="peer-detail"),
    path("alias/", AliasListView.as_view(), name="alias"),
    path("sub/", SubscriptionListView.as_view(), name="subscription"),
    path("SNRinfo/", getSNRjson, name="snr-info"),
    path("json/SNRinfo/", getSNRjson, name="snr-info"),
    path("json/state/<str:address>", getStatejson, name="state"),
    path("json/accounts/", TopAccountsJson, name="json-account"),
    path("json/accounts/<int:results>", TopAccountsJson),
    path("pools/", PoolListView.as_view(), name="pools"),
    path("pool/<str:id>", PoolDetailView.as_view(), name="pool-detail"),
    path("miner/", MinerListView.as_view(), name="miner"),
    path("forged-blocks/", ForgedBlocksListView.as_view(), name="forged-blocks"),
    # path("admin/", admin.site.urls),
    path("download/<str:ware>/", get_download, name="download"),
    path("download/", RedirectView.as_view(url="https://github.com/signum-network/"), name="download"),
]

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
        path("silk/", include("silk.urls", namespace="silk")),
    ]