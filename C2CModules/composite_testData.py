from testData.testData import *

composite_endpoint = '/composite-api/graphql'
composite_headers = {
    "Content-Type": "application/json",
    "api-key": "Y29tcG9zaXRlLWFwaUAxMjM",
    "x-requestor": "test"
}

getVehicleLocationBySystemId_payload = """
                query GetVehicleLocationBySystemId{
    getVehicleLocationBySystemId(systemId: <systemId>) {
        systemId
        vin
        model
        group
        lastTrackedStr
        lastTracked
        status
        address
        location {
            lat
            lng
        }
    }
}

             """

getVehicleLocations_payload = """
                query VehicleLocations {
    vehicleLocations(
        vehicleLocationFilter: {
            regionCode: <regionCode>
            countryCode: <countryCode>
            engineType: <engineType>
            model: <model>
            year: <year>
            variant: null
            search: null
            group: null
            vehicleStatus: null
            alertStatus: null
        }
        offset: 0
        limit: 10
    ) {
        offset
        limit
        totalRecords
        message
        vehicleLocationResponses {
            systemId
            vin
            model
            group
            lastTrackedStr
            lastTracked
            status
            address
            location {
                lat
                lng
            }
        }
    }
}

             """

getActiveActiveAlertCountsForVehicles_payload = """
                query ActiveAlertCountsForVehicles {
    activeAlertCountsForVehicles(
        vehicleGlobalFilter: {
            regionCode: <regionCode>
            countryCode: <countryCode>
            engineType: <engineType>
            model: <model>
            year: <year>
            variant: null
        }
    ) {
        vehicles
        status
        alerts
    }
}

                """

viewAlertCounts_payload = """
                query ViewAlertCounts {
    viewAlertCounts(
        alertDataFilterDTO: {
            regionCode: <regionCode>
            countryCode: <countryCode>
            engineType: <engineType>
            model: <model>
            year: <year>
            variant: null
            startTime: null
            endTime: null
        }
    ) {
        nonDTC
        DTC
        D0
        D1
        D2
        D3
        crashCount
        emergencyCount
    }
}
"""

getVehicleCountsByStatus_payload = """
                query VehicleCountsByStatus {
    vehicleCountsByStatus(
        vehicleGlobalFilter: {
            regionCode: <regionCode>
            countryCode: <countryCode>
            engineType: <engineType>
            model: <model>
            year: <year>
            variant: null
        }
    ) {
        vehicles
        status
        alerts
    }
}

             """

viewDtcTimeSeriesCounts_payload = """
                query ViewDtcTimeSeriesCounts {
    viewDtcTimeSeriesCounts(
        dtcStatsDataFilterDTO: {
            regionCode: <regionCode>
            countryCode: <countryCode>
            engineType: <engineType>
            model: <model>
            year: <year>
            variant: null
            duration: null
        }
    )
}

             """

viewNonDTCAlertDetailsForVehicle_payload = """
                query ViewNonDTCAlertDetailsForVehicle {
    viewNonDTCAlertDetailsForVehicle(
        systemId: <systemId>
        alertStatus: "ALL"
        startDate: null
        endDate: null
        offset: 0
        limit: 100
        category: "ALL"
    ) {
        offset
        limit
        totalRecords
        message
        nonDTCList {
            nonDTCType
            date
            ignitionStatus
            severity
            alertStatus
            location {
                longitude
                latitude
            }
        }
    }
}

             """

viewDTCAlertDetailsForVehicle_payload = """
                query ViewDTCAlertDetailsForVehicle {
    viewDTCAlertDetailsForVehicle(
        systemId: <systemId>
        dtcStatus: "ALL"
        endDate: null
        startDate: null
        offset: 0
        limit: 100
    ) {
        offset
        limit
        totalRecords
        message
        dTCList {
            dtc
            dtcCode
            dtcInfo
            firstOccurrence
            lastOccurrence
            runningTime
            noOfOccurrences
            dtcStatus
            ticketStatus
        }
    }
}
             """

viewVehicleDetailsWithAlerts_payload = """query ViewVehicleDetailsWithAlerts {
    viewVehicleDetailsWithAlerts(
        vehicleDetailsWithAlertsFilterDTO: {
            model: <model>
            variant: null
            year: <year>
            regionCode: <regionCode>
            countryCode: <countryCode>
            engineType: <engineType>
            vehicleStatus: null
            alertType: "ALL"
        }
        offset: 0
        limit: 100
    ) {
        offset
        limit
        totalRecords
        message
        vehiclesList {
            systemId
            vin
            model
            group
            lastTracked
            status
            vehicleHealth
            kmsTravelled
            dtcCount
            nonDTCCount
        }
    }
}
"""

getTripDetails_payload = """
        query GetTripDetails {
    getTripDetails(
        systemId: <systemId>
        startDate: null
        endDate: null
        offset: 0
        limit: 100
    ) {
        offset
        limit
        totalRecords
        message
        tripList {
            tripId
            systemId
            tripStatus
            tripStartDate
            tripEndDate
            tripDuration
            distance
            runningTime
            idlingTime
            overspeedCount
            averageSpeed
            topSpeed
            harshBreakers
            harshAcceleration
            navigation
            tripStartLoc {
                longitude
                latitude
                altitude
            }
            tripEndLoc {
                longitude
                latitude
                altitude
            }
        }
    }
}
 """
getTripReplayDetailsWithPagination_payload = """
        query GetTripReplayDetailsWithPagination {
    getTripReplayDetailsWithPagination(
        systemId: <systemId>
        tripId: <tripId>
        startDate: <startDate>
        endDate: <endDate>
    ) {
        offset
        limit
        totalRecords
        message
        tripId
    }
}


        """
getTripReplayDetails_payload = """
        query GetTripReplayDetails {
    getTripReplayDetails(
        systemId: <systemId>
        tripId: <tripId>
        startDate: <startDate>
        endDate: <endDate>
    ) {
        tripId
        plotPoints {
            time
            longitude
            latitude
            direction
            altitude
        }
        alerts {
            harshBreaks {
                time
                longitude
                latitude
                direction
                altitude
            }
            harshAcceleration {
                time
                longitude
                latitude
                direction
                altitude
            }
            overSpeed {
                time
                longitude
                latitude
                direction
                altitude
            }
        }
    }
}


        """
deleteTrip_payload = """
        query DeleteTrip {
            deleteTrip(
                systemId: <systemId>
                tripId: <tripId>
            )
        }
        """
mergeTrips_payload = """
        query MergeTrips {
            mergeTrips(systemId: "IMknCfR6qBhVmWVFyWHfS", tripIds: "IMknCfR6qBhVmWVFyWHfS_1755469304544,IMknCfR6qBhVmWVFyWHfS_1755469304544")
        }

        """
getVehicleOverviewBySystemId_payload = """
        query MergeTrips {
            getVehicleOverviewBySystemId(systemId: <systemId>) {
                systemId
                batteryLevel
                isLocked
                connectedStatus
                signalStrength
                odo
                ignition
                range
                mileage
                lastSyncTime
                vehicleMode
                charge {
                    soc
                    range
                }
                chargingStatus {
                    timeElapsed
                    timeRemaining
                    chargeType
                }
                vehicleLocationData {
                    lat
                    lng
                    gps
                    gsm
                    direction
                    lastSyncTime
                }
                vehicleStatus
                vehicleSettings {
                    abs
                    hillHold
                    traction
                    regen
                    cruiseControl
                    jumblePIN
                }
                clusterSettings {
                    distance
                    temperature
                    time
                    language
                }
                rideModeConfig {
                    mode
                    custom {
                        abs
                        tc
                        pow
                        tm
                        rc
                        rb
                    }
                }
                trips {
                    trip
                    ResetTimestamp
                    Distance
                    Duration
                    MaxSpeed
                    AverageSpeed
                    Instant
                    averageEfficiency
                    totalEnergy
                }
                geofence {
                    type
                    radius
                    geoCoordinates
                }
                ota {
                    currentVersion
                    updatedTimeStamp
                    newVersion {
                        versionDetails
                        versionDescription
                    }
                }
                tpms {
                    frontPressure
                    rearPressure
                    frontTemp
                    rearTemp
                    Battery
                }
            }
        }

        """
getGeoFenceBySystemId_payload = """       
        query GetGeoFenceBySystemId {
            getGeoFenceBySystemId(systemId: <systemId>) {
                geoId
                geofenceType
                radius
                name
                active
                geoCoordinates
            }
        }

        """
getGeoFencesBySystemId_payload = """       
            query GetGeoFencesBySystemId {
    getGeoFencesBySystemId(
        systemId: <systemId>
        geoId: null
        name: null
    ) {
        geoId
        geofenceType
        radius
        name
        active
        geoCoordinates
    }
}

        """


