START
  LOAD households from "households.txt" into a list
  LOAD floods from "floods.txt" into a list
  IF files do not exist, start with empty lists

  REPEAT
    SHOW menu (1 Register, 2 Check readiness, 3 Log flood,
    4 Street summary, 5 Search, 6 Exit)
    ASK user for choice

    IF choice = 1:
      ASK name, street, member count, vulnerable counts
      VALIDATE name not blank, members >= 0, vulnerable <= members
      IF invalid: SHOW error, back to menu
      GENERATE household id
      ADD household to list
      SAVE list to file
      SHOW "Registered with id <id>"

    ELSE IF choice = 2:
      ASK household name or id
      IF not found: SHOW "No matching household", back to menu
      ASK rainfall (light/moderate/heavy)
      ASK river level (normal/alert/alarm/critical)
      VALIDATE both values are accepted

      readiness = 1
      IF river = "critical": readiness = 4
      ELSE IF river = "alarm":
        IF rainfall = "heavy": readiness = 4 ELSE readiness = 3
      ELSE IF river = "alert":
        IF rainfall = "heavy": readiness = 3 ELSE readiness = 2
      ELSE IF rainfall = "heavy": readiness = 2

      LOOK UP action text and base checklist for readiness
      IF household has children: ADD child items
      IF household has elderly: ADD medicine/mobility items
      IF household has PWD: ADD assistance items
      SHOW readiness, reason, action, household summary, checklist

    ELSE IF choice = 3:
      ASK household name or id
      IF not found: SHOW "No matching household", back to menu
      ASK flood date, depth (cm), duration (hrs)
      VALIDATE depth >= 0 and duration >= 0
      ADD flood record to log
      SAVE log to file
      SHOW "Flood event recorded"

    ELSE IF choice = 4:
      count flood events per street
      SORT streets by count, highest first
      SHOW each street with count and most recent date

    ELSE IF choice = 5:
      ASK name or street to search
      COLLECT households whose name or street contains the text
      IF none: SHOW "No matches found"
      ELSE SHOW each match with id and street

    ELSE IF choice = 6:
      SHOW "Data saved. Exiting."
      STOP

    ELSE:
      SHOW "Invalid choice. Enter 1 to 6."
  END REPEAT
END

