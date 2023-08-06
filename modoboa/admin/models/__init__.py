"""Admin models."""

from .alarm import Alarm
from .alias import (
    Alias,
    AliasRecipient,
    validate_alias_address,
    modify_or_create_alias,
    remove_recipient_from_alias)
from .base import AdminObject
from .domain import Domain
from .domain_alias import DomainAlias
from .mailbox import Mailbox, MailboxOperation, Quota, SenderAddress
from .mxrecord import DNSBLResult, MXRecord

__all__ = [
    "Alarm",
    "AdminObject",
    "Alias",
    "AliasRecipient",
    "DNSBLResult",
    "Domain",
    "DomainAlias",
    "Mailbox",
    "MailboxOperation",
    "MXRecord",
    "Quota",
    "SenderAddress",
    "validate_alias_address",
    "modify_or_create_alias",
    "remove_recipient_from_alias",
]
