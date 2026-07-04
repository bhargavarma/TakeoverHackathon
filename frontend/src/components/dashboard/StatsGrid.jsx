import GlassCard from "../ui/GlassCard";
import {
IndianRupee,
TrendingUp,
ShoppingCart,
Boxes
} from "lucide-react";

export default function StatsGrid(){

return(

<div className="grid lg:grid-cols-4 gap-6">

<GlassCard
icon={<IndianRupee size={30}/>}
title="Revenue"
value="₹1.24L"
/>

<GlassCard
icon={<TrendingUp size={30}/>}
title="Profit"
value="₹31.8K"
/>

<GlassCard
icon={<Boxes size={30}/>}
title="Inventory"
value="184"
/>

<GlassCard
icon={<ShoppingCart size={30}/>}
title="Orders"
value="96"
/>

</div>

)

}