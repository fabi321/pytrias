from typing import List
from xml.etree import ElementTree
from elementpath import select
import XPaths
from XPaths import construct_simple_xpath, construct_complex_xpath
from Classes.Line import Line
from Classes.Response import Response
from Classes.StopWithoutLine import StopWithoutLine


class StopResponse(Response):
    def __init__(self, elements: List[ElementTree.ElementTree], **kwargs):
        Response.__init__(self, elements, **kwargs)
        self._lines: [List[Line], None] = None

    def _get_lines(self):
        self._lines_trias_id: List[str] = select(self._elements, construct_simple_xpath(False, False, False, XPaths.line_trias_id), namespaces=self._namespaces)
        self._lines_number: List[str] = select(self._elements, construct_simple_xpath(False, False, False, XPaths.line_number), namespaces=self._namespaces)
        self._lines_string: List[str] = select(self._elements, construct_simple_xpath(False, False, False, XPaths.line_string), namespaces=self._namespaces)
        self._lines_start: List[str] = select(self._elements, construct_simple_xpath(False, False, False, XPaths.line_start), namespaces=self._namespaces)
        self._lines_start_name: List[str] = select(self._elements, construct_simple_xpath(False, False, False, XPaths.line_start_name), namespaces=self._namespaces)
        self._lines_end: List[str] = select(self._elements, construct_simple_xpath(False, False, False, XPaths.line_end), namespaces=self._namespaces)
        self._lines_end_name: List[str] = select(self._elements, construct_simple_xpath(False, False, False, XPaths.line_end_name), namespaces=self._namespaces)
        self._lines: List[Line] = []
        for i in range(len(self._lines_trias_id)):
            trias_id: str = self._lines_trias_id[i]
            number: int = int(self._lines_number[i])
            string: str = self._lines_string[i]
            line: Line = Line(number, string, trias_id)
            line.add_stop(StopWithoutLine(self._lines_start[i], self._lines_start_name[i]))
            line.add_stop(StopWithoutLine(self._lines_end[i], self._lines_end_name[i]))
            self._lines.append(line)

    def get_lines(self) -> List[Line]:
        if not self._lines:
            self._get_lines()
        return self._lines

    def __len__(self) -> int:
        if not self._lines:
            self._get_lines()
        return len(self._lines)
