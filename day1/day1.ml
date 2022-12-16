let file = Sys.argv.(1);;

let data =
    In_channel.with_open_bin file In_channel.input_all
    |> String.split_on_char '\n'

let max_list l =
    if List.length l = 0 then -1
    else List.fold_left Stdlib.max (List.hd l) (List.tl l)

let part_1 data =
    let rec solve acc acclist data =
        match data with
        | [] -> max_list acclist
        | h::t ->
                if String.compare h "" = 0 then solve 0 (acc::acclist) t
                else solve (acc + int_of_string h) acclist t
    in solve 0 [] data

let part_2 data =
    let rec solve acc acclist data =
        match data with
        | [] ->
                let l = List.rev (List.sort Int.compare acclist) in
                (match l with
                | x1::x2::x3::t -> x1 + x2 + x3
                | _ -> failwith "expecting more than 3 values")
        | h::t ->
                if String.compare h "" = 0 then solve 0 (acc::acclist) t
                else solve (acc + int_of_string h) acclist t
    in solve 0 [] data


let () = Printf.printf "%d\n%d\n" (part_1 data) (part_2 data)
