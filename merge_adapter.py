

def lambda_handler(event, null):
    registration_number_data = event[0]
    photo_data = event[1]
    exif_data = photo_data['exif']
    gps_data = photo_data['gpsinfo']
    photo_location_data = event[2]
    device = exif_data['Make'] + ' ' + exif_data['Model']

    gps_attributes = dict([(gps_key, gps_data[gps_key])
                           for gps_key in gps_data])
    key = photo_location_data['key']
    bucket = photo_location_data['bucket']
    version_id = photo_location_data['version-id']
    input_data = {
        'registration-number': registration_number_data['text'] if 'TEXT_FOUND' == registration_number_data['recognitionCode'] else "UNKNOWN",
        'timestamp': exif_data['DateTime'] + '-' + str(abs(hash(bucket + key + version_id))),
        'bucket': bucket,
        'key': key,
        'version-id': version_id,
        'device': device,
    }

    input_data.update(gps_attributes)

    return {
        'action': 'save',
        'input': input_data
    }
