---
title: Updater
layout: api

---

### Public attributes

{: .table .table-striped .table-condensed}
| type   | name     |
|:-------|:---------|



### Public functions

{: .table .table-striped .table-condensed}
| type   | name     |
|:-------|:---------|
| void | progress(int step, int total_step, float score) const =0 |
| void | message(std::string) const =0 |
| void | message(boost::format) const =0 |
| bool | cancelled() const =0 |

