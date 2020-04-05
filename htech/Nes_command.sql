--Reset or fresh migration all--
python manage.py reset_migrations permission roleUser role account company staff guard attendance booking duty building
--migration all--
python manage.py makemigrations permission roleUser role account company staff guard attendance booking duty building

-- jdbc:mysql://localhost:3306/hospital_manage?useUnicode=true&useJDBCCompliantTimezoneShift=true&useLegacyDatetimeCode=false&serverTimezone=UTC