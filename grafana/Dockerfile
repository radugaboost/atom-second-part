FROM grafana/grafana

ENV GF_AUTH_DISABLE_LOGIN_FORM "true"
ENV GF_AUTH_ANONYMOUS_ENABLED "true"
ENV GF_AUTH_ANONYMOUS_ORG_ROLE "Admin"

ADD provisioning /etc/grafana/provisioning
ADD grafana.ini /etc/grafana/grafana.ini
ADD dashboards /etc/grafana/dashboards
