---
title: WorkUnit
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
| None | WorkUnit(const string &system, const string &integrator, const string &state, int step_chunk) |
| None | WorkUnit(const string &wu_name) |
| None | WorkUnit(const fs::path &wu_path) |
| int | step_chunk() const  |
| void | set_step_chunk(const int step_chunk) |
| const string | system_fn() const  |
| const string | integrator_fn() const  |
| const string | state_fn() const  |
| const string & | codename() const  |
| const string & | fullname() const  |
| const string & | description() const  |

