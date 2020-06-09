# streams: API URL endpoints to be called
# properties:
#   <root node>: Plural stream name for the endpoint
#   path: API endpoint relative path, when added to the base URL, creates the full path
#   key_properties: Primary key field(s) for the object endpoint
#   replication_method: FULL_TABLE or INCREMENTAL
#   replication_keys: bookmark_field(s), typically a date-time, used for filtering the results
#        and setting the state
#   params: Query, sort, and other endpoint specific parameters
#   data_key: JSON element containing the records for the endpoint
#   bookmark_query_field: Typically a date-time field used for filtering the query
#   bookmark_type: Data type for bookmark, integer or datetime
#   children: A collection of child endpoints (where the endpoint path includes the parent id)
#   parent: On each of the children, the singular stream name for parent element
STREAMS = {
    'assets': {
        'key_properties': ['id'],
        'replication_method': 'INCREMENTAL',
        'data_key': 'assets',
        'bookmark_type': 'datetime',
        'replication_keys': ['last_modified_date']
    },
    'data_items': {
        'key_properties': ['id'],
        'replication_method': 'INCREMENTAL',
        'data_key': 'data_items'
    },
    'funds': {
        'key_properties': ['id'],
        'replication_method': 'INCREMENTAL',
        'data_key': 'funds',
        'payload_ref': 'NamedEntity',
        "bookmark_type": "datetime",
        'replication_keys': ['last_modified_date']
    },
    'investment_transactions': {
        'key_properties': ['id'],
        'replication_method': 'INCREMENTAL',
        'replication_keys': ['last_modified'],
        'data_key': 'investment_transactions'
    },
    'investments': {
        'key_properties': ['id'],
        'replication_method': 'INCREMENTAL',
        'replication_keys': ['last_modified_date'],
        'data_key': 'investments',
        'bookmark_type': 'datetime'
    },
    'scenarios': {
        'key_properties': ['id'],
        'replication_method': 'INCREMENTAL',
        'data_key': 'scenarios'
    },
    'securities': {
        'key_properties': ['id'],
        'replication_method': 'INCREMENTAL',
        'replication_keys': ['last_modified_date'],
        'data_key': 'securities'
    },
    'asset_periodic_data': {
        'key_properties': ['currency_code', 'data_item_id', 'entity_path', 'standardized_data_id', 'scenario_id'],
        'replication_method': 'INCREMENTAL',
        'data_key': 'asset_periodic_data',
        'bookmark_type': 'datetime'
    },
    'fund_periodic_data': {
        'key_properties': ['currency_code', 'data_item_id', 'entity_path', 'standardized_data_id', 'scenario_id'],
        'replication_method': 'INCREMENTAL',
        'data_key': 'fund_periodic_data',
        'bookmark_type': 'datetime'
    },
    'data_item_periodic_data': {
        'key_properties': [],
        'replication_method': 'INCREMENTAL',
        'data_key': 'data_item_periodic_data'
    },
    'security_periodic_data': {
        'key_properties': [],
        'replication_method': 'INCREMENTAL',
        'data_key': 'data_item_periodic_data'
    },
    'fund_to_asset_relations': {
        'key_properties': ['id'],
        'replication_method': 'INCREMENTAL',
        'data_key': 'fund_to_asset_relations'
    },
    'fund_to_fund_relations': {
        'key_properties': ['id'],
        'replication_method': 'INCREMENTAL',
        'data_key': 'fund_to_fund_relation'
    },
    'asset_to_asset_relations': {
        'key_properties': ['id'],
        'replication_method': 'INCREMENTAL',
        'data_key': 'asset_to_asset_relations'
    },
    'asset_periodic_data_standardized': {
        'key_properties': ['standardized_data_id','data_item_id'],
        'replication_method': 'INCREMENTAL',
        'data_key': 'asset_periodic_data_standardized'
    },
    'fund_periodic_data_standardized': {
        'key_properties': ['standardized_data_id','data_item_id'],
        'replication_method': 'INCREMENTAL',
        'data_key': 'fund_periodic_data_standardized'
    }
}

def flatten_streams():
    flat_streams = {}
    # Loop through parents
    for stream_name, endpoint_config in STREAMS.items():
        flat_streams[stream_name] = {
            'key_properties': endpoint_config.get('key_properties'),
            'replication_method': endpoint_config.get('replication_method'),
            'replication_keys': endpoint_config.get('replication_keys')
        }
        # Loop through children
        children = endpoint_config.get('children')
        if children:
            for child_stream_name, child_enpoint_config in children.items():
                flat_streams[child_stream_name] = {
                    'key_properties': child_enpoint_config.get('key_properties'),
                    'replication_method': child_enpoint_config.get('replication_method'),
                    'replication_keys': child_enpoint_config.get('replication_keys')
                }
    return flat_streams
