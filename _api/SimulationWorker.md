---
title: SimulationWorker
layout: api

---

### Public attributes

{: .table .table-striped .table-condensed}
| type   | name     |
|:-------|:---------|
| bool | is_cancelled |
| std::mutex | cancelled_mutex |



### Public functions

{: .table .table-striped .table-condensed}
| type   | name     |
|:-------|:---------|
| None | SimulationWorker() |
| void | progress(int i, int num_steps, float score) const  |
| void | message(std::string) const  |
| void | message(boost::format) const  |
| bool | cancelled() const  |

