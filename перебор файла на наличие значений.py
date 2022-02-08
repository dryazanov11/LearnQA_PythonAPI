# -*- coding: utf-8 -*-
import json

text = '{"resourceType":"Patient","id":"adee3359-894a-4eee-83d5-656a82263070","meta":{"versionId":"v9c55ba0-c3cb-4050-a087-281a17b66294","lastUpdated":"2022-01-13T11:15:45.276391+00:00"},"extension":[{"url":"http://hl7.org/fhir/StructureDefinition/birthPlace","valueAddress":{"text":"г. Ютеборг, ГДР"}}],"identifier":[{"system":"urn:oid:1.2.643.5.1.13.2.7.100.5","value":"ID_Pac_MIS_13221194_27","assigner":{"display":"1.2.643.2.69.1.2.6"}},{"system":"urn:oid:1.2.643.2.69.1.1.1.6.14","value":"7816:726279","assigner":{"display":"ОУФМС по РФ в г. Санкт-Петербург, 100-001, 26.10.2008"}},{"system":"urn:oid:1.2.643.2.69.1.1.1.6.3","value":"IVXL-АБ:744233","assigner":{"display":"ЗАГС г. Санкт-Петербург"}},{"system":"urn:oid:1.2.643.2.69.1.1.1.6.223","value":"17400354229","assigner":{"display":"ПФР"}},{"system":"urn:oid:1.2.643.2.69.1.1.1.6.240","value":"7800010250","assigner":{"display":"РОСНО-МС"}},{"system":"urn:oid:1.2.643.2.69.1.1.1.6.228","value":"5598718357093420","assigner":{"display":"1.2.643.5.1.13.2.1.1.635.22001"}}],"name":[{"family":"Хохлыкина","given":["Инна","Андреевна"]}],"gender":"female","birthDate":"1999-03-20","address":[{"extension":[{"url":"http://n3.zdrav.netrika.ru/StructureDefinition/","valueCode":"1"}],"use":"home","text":"Ленинградская область, п. Мурино, ул.Оптиков, д.6, кв.101","line":["ул.Оптиков, д.6, кв.101"],"city":"п. Мурино","district":"Всеволожский район","state":"47","postalCode":"185030"},{"use":"temp","text":"Ленинградская область, п. Мурино, ул.Привокзальная, д.6, кв.101","line":["ул.Привокзальная, д.6, кв.101"],"city":"п. Мурино","district":"Всеволожский район","state":"47","postalCode":"185035"}],"managingOrganization":{"reference":"Organization/01cf8e37-1e5a-991f-77f0-078450d5e0d9"}}'
json_text = json.loads(text)
try:
    i = 0
    while i >= 0:
        key = json_text['identifier'][i]['value']
        print(key)
        i += 1
except IndexError:
    print('Все значения обработаны')