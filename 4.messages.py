import enum
from dataclasses import dataclass
from abc import ABC, abstractmethod

class MessageType(enum.Enum):
    TELEGRAM = enum.auto()
    MATTERMOST = enum.auto()
    SLACK = enum.auto()

@dataclass
class JsonMessage:
    message_type: MessageType
    payload: str


@dataclass
class ParseMessage:
    text: str
    sender: str
    timestamp: str

class BaseParser(ABC):
    @abstractmethod
    def parse(self, msg:JsonMessage) ->ParsedMessage:
        ...


class TelegramParser(BaseParser):
    def parse(self, msg: JsonMessage) -> ParsedMessage:
        ...


class MattermostParser(BaseParser):
    def parse(self, msg: JsonMessage) -> ParsedMessage:
        ...

class SlackParser(BaseParser):
    def parse(self, msg: JsonMessage) -> ParsedMessage:
        ...


class ParserFactory:
    _parsers: dict[MessageType, BaseParser] = {
        MessageType.TELEGRAM: TelegramParser(),
        MessageType.MATTERMOST: MattermostParser(),
        MessageType.SLACK: SlackParser(),
    }

    def parse(self, msg: JsonMessage) -> ParseMessage:
        parser = self._parsers[msg.message_type]
        return parser.parse(msg)