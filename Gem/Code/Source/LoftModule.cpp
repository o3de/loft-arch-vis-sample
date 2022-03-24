
#include <AzCore/Memory/SystemAllocator.h>
#include <AzCore/Module/Module.h>

#include "LoftSystemComponent.h"

namespace Loft
{
    class LoftModule
        : public AZ::Module
    {
    public:
        AZ_RTTI(LoftModule, "{590484da-b784-4b2a-9442-4f333ef9ad6c}", AZ::Module);
        AZ_CLASS_ALLOCATOR(LoftModule, AZ::SystemAllocator, 0);

        LoftModule()
            : AZ::Module()
        {
            // Push results of [MyComponent]::CreateDescriptor() into m_descriptors here.
            m_descriptors.insert(m_descriptors.end(), {
                LoftSystemComponent::CreateDescriptor(),
            });
        }

        /**
         * Add required SystemComponents to the SystemEntity.
         */
        AZ::ComponentTypeList GetRequiredSystemComponents() const override
        {
            return AZ::ComponentTypeList{
                azrtti_typeid<LoftSystemComponent>(),
            };
        }
    };
}// namespace Loft

AZ_DECLARE_MODULE_CLASS(Gem_Loft, Loft::LoftModule)
