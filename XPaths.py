stoerung: str = "for $x in //StopEvent[descendant::EstimatedTime]/descendant::*[local-name(.)='SituationNumber'] return //PtSituation[*[local-name(.)='SituationNumber'] = $x]/*[local-name(.)='Description']"
location_lon: str = "//GeoPosition/Longitude/text()"
location_lat: str = "//GeoPosition/Latitude/text()"
prefix: str = "(//TripResult[descendant::Service[count(ServiceSection) = 1]/ServiceSection[Mode/PtMode = 'tram']$LINEREF])"
first: str = "[1]"
lons: str = "/descendant::Projection/Position/Longitude/text()"
lats: str = "/descendant::Projection/Position/Latitude/text()"
stops: str = "/descendant::TimedLeg/*/StopPointRef/text()"#replace(.,'([a-z]*:[0-9]*:[0-9]*):.*','$1')"
stop_names: str = "/descendant::TimedLeg/*/StopPointName/Text/text()"
line_number: str = "/descendant::ServiceSection/PublishedLineName/Text/text()"
line_string: str = "/descendant::ServiceSection/normalize-space(RouteDescription/Text)"
line_trias_id: str = "/descendant::ServiceSection/LineRef/text()"
line_start: str = "/descendant::ServiceSection/../OriginStopPointRef/text()"#replace(., '([a-z]*:[0-9]*:[0-9]*):.*', '$1')"
line_start_name: str = "/descendant::ServiceSection/../OriginText/Text/text()"#replace(., '([a-z]*:[0-9]*:[0-9]*):.*', '$1')"
line_end: str = "/descendant::ServiceSection/../DestinationStopPointRef/text()"#replace(., '([a-z]*:[0-9]*:[0-9]*):.*', '$1')"
line_end_name: str = "/descendant::ServiceSection/../DestinationText/Text/text()"#replace(., '([a-z]*:[0-9]*:[0-9]*):.*', '$1')"
stop_name_ref: str = "/descendant::StopPointRef/text()"
stop_name_lon: str = "/descendant::Longitude/text()"
stop_name_lat: str = "/descendant::Latitude/text()"
stop_name_name: str = "/descendant::StopPointName/Text/text()"


def construct_xpath(trip: bool, lineref: bool, single: bool, original_string) -> str:
    if trip:
        temp_pre = prefix
    else:
        temp_pre = prefix.replace('TripResult', 'StopEventResult')
    if lineref:
        temp_pre = temp_pre.replace('$LINEREF', "[descendant::LineRef='$LINEREF']")
    else:
        temp_pre = temp_pre.replace('$LINEREF', '')
    if single:
        return temp_pre + first + original_string
    return temp_pre + original_string
