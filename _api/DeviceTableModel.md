---
title: DeviceTableModel
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
| None | DeviceTableModel() |
| int | rowCount(const QModelIndex &parent) const  |
| int | columnCount(const QModelIndex &parent) const  |
| QVariant | data(const QModelIndex &index, int role) const  |
| QVariant | headerData(int section, Qt::Orientation orientation, int role) const  |
| [Device]({{site.url}}/) | entries() const  |
| const std::vector< std::runtime_error > & | errors() const  |

