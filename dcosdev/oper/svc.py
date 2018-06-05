template = """
name: {{FRAMEWORK_NAME}}
scheduler:
  principal: {{FRAMEWORK_PRINCIPAL}}
  user: {{FRAMEWORK_USER}}
pods:
  %(template)s:
    count: {{NODE_COUNT}}
    placement: '{{{NODE_PLACEMENT}}}'
    {{#ENABLE_VIRTUAL_NETWORK}}
    networks:
      {{VIRTUAL_NETWORK_NAME}}:
        labels: {{VIRTUAL_NETWORK_PLUGIN_LABELS}}
    {{/ENABLE_VIRTUAL_NETWORK}}
    tasks:
      node:
        goal: RUNNING
        cmd: "echo %(template)s >> %(template)s-container-path/output && sleep $SLEEP_DURATION"
        cpus: {{NODE_CPUS}}
        memory: {{NODE_MEM}}
        volume:
          path: "%(template)s-container-path"
          type: {{NODE_DISK_TYPE}}
          size: {{NODE_DISK}}
        env:
          SLEEP_DURATION: {{SLEEP_DURATION}}
"""
