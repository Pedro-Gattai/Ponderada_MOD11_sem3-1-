#!/bin/bash

set -e

echo "Starting init script for ClickHouse..."

# Cópia do users.xml para um diretório temporário
echo "Copying users.xml to temporary location..."
cp /etc/clickhouse-server/users.xml /tmp/users.xml

# Substitui as variáveis no arquivo temporário
echo "Replacing variables in the temporary users.xml file..."
sed -i "s/{{CLICKHOUSE_USER}}/${CLICKHOUSE_USER}/g" /tmp/users.xml
sed -i "s/{{CLICKHOUSE_PASSWORD}}/${CLICKHOUSE_PASSWORD}/g" /tmp/users.xml

# Substitui o original pelo modificado
echo "Replacing the original users.xml with the modified version..."
cp /tmp/users.xml /etc/clickhouse-server/users.xml

# Inicia o ClickHouse
echo "Starting ClickHouse service..."
exec /entrypoint.sh
