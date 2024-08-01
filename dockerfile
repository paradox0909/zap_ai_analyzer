FROM zaproxy/zap-stable

ENV ZAP_API_KEY=paradox0909
EXPOSE 8090
ENTRYPOINT ["zap.sh", "-daemon", "-port", "8090", "-host", "0.0.0.0", "-config", "api.addrs.addr.name=.*", "-config", "api.addrs.addr.regex=true", "-config", "api.key=paradox0909"]
