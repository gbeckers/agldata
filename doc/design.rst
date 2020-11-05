Design considerations
---------------------
We chose YAML as format for data because it is universal and very easy to
write and edit by hand. JSON would have been simpler for installation
reasons as it is included in the standard library, while YAML depends on an
external library, pyyaml. However, JSON requires more brackets etc, making it
more error prone for use by humans who enter data. We want to minimize such
errors.
