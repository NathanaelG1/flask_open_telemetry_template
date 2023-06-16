#Run
opentelemetry-instrument \
    --traces_exporter console \
    --metrics_exporter console \
    flask run -p 8080