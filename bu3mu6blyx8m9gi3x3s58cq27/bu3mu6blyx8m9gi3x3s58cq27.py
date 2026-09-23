from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import (
    OTLPSpanExporter as OtlpSpanExporter,
)
from opentelemetry.instrumentation.logging import LoggingInstrumentor


LoggingInstrumentor().instrument(set_logging_format=False)

provider: TracerProvider = TracerProvider()
provider.add_span_processor(BatchSpanProcessor(OtlpSpanExporter()))
trace.set_tracer_provider(provider)


def bu3mu6blyx8m9gi3x3s58cq27() -> trace.Tracer:
    return trace.get_tracer("default")
