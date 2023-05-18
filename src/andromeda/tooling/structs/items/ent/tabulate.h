//-*-C++-*-

#ifndef ANDROMEDA_STRUCTS_ITEMS_ENT_TABULATE_H_
#define ANDROMEDA_STRUCTS_ITEMS_ENT_TABULATE_H_

namespace andromeda
{

  template<typename index_type>
  void create_hash_to_name(std::vector<base_entity>& entities,
                           std::map<index_type, std::string>& hash_to_name)
  {
    hash_to_name.clear();
    for(const auto& ent:entities)
      {
        hash_to_name.insert({ent.hash, ent.name});
      }
  }

  std::string tabulate(std::vector<base_entity>& entities)
  {
    std::sort(entities.begin(), entities.end());

    std::stringstream ss;

    std::vector<std::string> headers={};

    if(entities.size()==0)
      {
        ss << "\nentities: " << entities.size() << "\n";
        return ss.str();
      }
    else if(entities.at(0).subj_name==PARAGRAPH)
      {
        headers = base_entity::short_text_headers();
      }
    else if(entities.at(0).subj_name==TABLE)
      {
        headers = base_entity::short_table_headers();
      }
    else
      {
	LOG_S(ERROR) << "not supported subject-type";
	return "";
      }

    std::vector<std::vector<std::string> > data={};

    std::size_t col_width=32;
    for(auto& ent:entities)
      {
        auto row = ent.to_row(col_width);
        if(row.size()==headers.size())
          {
            data.push_back(ent.to_row(col_width));
          }
      }

    ss << "\nentities: " << entities.size() << "\n"
       << utils::to_string(headers, data);

    return ss.str();
  }

  std::string tabulate(std::string text, std::vector<base_entity>& entities)
  {
    std::sort(entities.begin(), entities.end(),
              [](const base_entity& lhs, const base_entity& rhs)
              {
                if(lhs.char_range[0]==rhs.char_range[0])
                  {
                    return lhs.char_range[1]>rhs.char_range[1];
                  }

                return lhs.char_range[0]<rhs.char_range[0];
              });

    std::vector<std::string> header = base_entity::short_text_headers();
    std::vector<std::vector<std::string> > data={};

    //std::size_t col_width=64;
    std::size_t name_width = 32;
    std::size_t orig_width = 48;

    for(auto& ent:entities)
      {
        data.push_back(ent.to_row(text, name_width, orig_width));
      }

    std::stringstream ss;
    if(entities.size()==0)
      {
        ss << "\nentities: " << entities.size() << "\n";
      }
    else
      {
        ss << "\nentities: " << entities.size() << "\n"
           << utils::to_string(header, data);
      }

    return ss.str();
  }

}

#endif
