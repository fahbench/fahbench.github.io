---
title: Device
layout: api

---

### Public attributes

{: .table .table-striped .table-condensed}
| type   | name     |
|:-------|:---------|
| std::string | platform_version |
| std::string | device_version |



### Public functions

{: .table .table-striped .table-condensed}
| type   | name     |
|:-------|:---------|
| None | Device(const std::string &platform, const std::string &device, int device_id, int platform_id=0) |
| const std::string & | device() const  |
| int | device_id() const  |
| int | platform_id() const  |
| const std::string & | platform() const  |

