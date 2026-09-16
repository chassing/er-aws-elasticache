from er_aws_elasticache.app_interface_input import ElasticacheData

MINIMAL_REQUIRED_FIELDS = {
    "region": "us-east-1",
    "identifier": "test-minimal",
    "output_prefix": "test-minimal-elasticache",
    "engine": "valkey",
    "engine_version": "7.2",
    "node_type": "cache.t4g.micro",
    "replication_group_id": "test-minimal",
}


def test_transit_encryption_enabled_defaults_to_false_not_none() -> None:
    """Regression test.

    main.tf/transit_encryption_staging.tf use this value as
    a boolean *condition* (`var.transit_encryption_enabled ? ... : null` / `&&`),
    which crashes Terraform with "Error: Null condition" if it's ever null.
    Every existing fixture (production tenant configs, this repo's own test
    fixtures) always sets this field explicitly, so a None default here was
    never actually exercised until a tenant configured with just the required
    fields hit it for real.
    """
    data = ElasticacheData(**MINIMAL_REQUIRED_FIELDS)

    assert data.transit_encryption_enabled is False
