"""Prometheus metrics that are exposed by REST API."""

from prometheus_client import Counter, Histogram, Info, make_asgi_app

rest_api_calls_total = Counter(
    "rest_api_calls_total", "REST API calls counter", ["path", "status_code"]
)

response_duration_seconds = Histogram(
    "response_duration_seconds", "Response durations", ["path"]
)

llm_calls_total = Counter("llm_calls_total", "LLM calls counter", ["provider", "model"])
llm_calls_failures_total = Counter("llm_calls_failures_total", "LLM calls failures")
llm_calls_validation_errors_total = Counter(
    "llm_validation_errors_total", "LLM validation errors"
)

llm_token_sent_total = Counter(
    "llm_token_sent_total", "LLM tokens sent", ["provider", "model"]
)
llm_token_received_total = Counter(
    "llm_token_received_total", "LLM tokens received", ["provider", "model"]
)

# expose selected provider and model
# (these are represented by counters, but the only meaning is presence of label)
selected_provider = Info("selected_provider", "Selected provider")
selected_model = Info("selected_model", "Selected model")

# register metric
metrics_app = make_asgi_app()
